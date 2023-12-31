===========
Epic Cycles
===========

// The user can:
// - click (or click and move) to add points.
// - press up and down arrows to change the number of gears.
// - keep pressing up to change the color of the drawn path.
// - press left to show or hide the lines drawn by intermediate gears.
// - press right to clear the scene and start a new epicycloid.

// m : mouse down flag.
m = 0;

// On mouse down: set m.
onmousedown = e => m = 1;

// On mouse move: if the mouse is down, recompute the epicycloid with the current mouse coordinates.
onmousemove = e => m && f(e);

// On mouse up: recompute the epicycloid with the current mouse coordinates and unset m.
onmouseup = e => (m = 0, f(e));

// When an arrow key is pressed, one of these four functions is called:
onkeydown = e => [

  // Left arrow (keyCode 37): toggle D (the multiple path flag).
  e => D ^= 1,
  
  // Up arrow (keyCode 38): increase Q (the max number of gears to draw).
  e => Q++,
  
  // Right arrow (keyCode 39): clear p (the points coordinates), G (the gears), and recompute the epicycloid (to reset everything else).
  e => (p = [], G = [], f()),
  
  // Down arrow (keyCode 40): decrease Q.
  e => Q--

// Execute the function stored at the index e.which - 37 (same as e.keyCode - 37).
][e.which - 37]();

// p is a 2D array representing the X and Y coordinates of each point.
p = [];

// By default (on load), a pattern representing JS1K is drawn. 
// This pattern is made of 33 points:

/*
p = [
 [0,0], [1,0], [1,3], [0,3], [0,2], [0,3], [1,3], [1,0], // J
 [4,0], [2,0], [2,1], [4,2], [4,3], [2,3], // S
 [5,3], [5,0], [4,1], [5,0], [5,3], [6,3], // 1
 [6,0], [6,2], [7,1], [6,2], [7,3], [6,2], [6,3], // K
 [4,3], [4,2], [2,1], [2,0], [1,0], [1,0] // Return at the beginning
]
*/

// Each pair of coordinates was encoded in the bits of an ASCII char in the form "0b10xxxyy" ("10" + 3 bits for X + 2 bits for Y).
// The "10" prefix is used to produce chars that are high enough in the ASCII range (64 to 96) because chars 0 to 32 are required by RegPack to compress the demo.
// The code below decodes X and Y from each character of the string "@DGCBCGDPHIRSKWTQTW[XZ]Z_Z[SRIHHH" and adds a multiplier and an offset to have a correct sizing and centering.
for(i of`@DGCBCGDPHIRSKWTQTW[XZ]Z_Z[SRIHDD`)
  p.push([50 * (i.charCodeAt() >> 2) - 950, 50 * (i.charCodeAt() & 3) - 90]);

// f()
// This function adds a point in p (is the e parameter is set) and recomputes all the gears' sizes and positions.
f = e => {

  // if e is set,
  e
  
  &&
  
  // and if p is empty, or if the distance between the mouse coordinates (e.x, e.y) and the last item of p is greater than 9px:
  // (this is done to avoid drawing points too close to each other when we click and move the mouse slowly.)
  (!p.length || Math.hypot(
    e.x - a.width / 2 - p[p.length - 1][0],
    e.y - a.height / 2 - p[p.length - 1][1]
  ) > 9)
  
  &&
  
  // Add the mouse coordinates to p.
  // The coordinates are adjusted to take into account that [0;0] is at the center of the canvas.
  p.push([e.x - a.width / 2, e.y - a.height / 2]);
  
  // p is deep-copied into P.
  // p is kept unchanged to draw the points on the canvas at each frame and to add new points with the mouse,
  // while P will be transformed into a list of Fourier coefficients.
  P = p.map(e => [...e]);
  
  // Reset Z (the list of points that will be drawn by each gear of the epicycloid).
  Z = [];
  
  // Set the body's bgColor to 0 (this gives a black background to the page).
  // Also, reset i (the loop var), D (the multiple line flag) and T (the time counter).
  // This loop here fills each gap between two points of P with a new point, placed at the center of the two surrounding points.
  // It stops when P has a length that is equal to a power of two.
  // This "power of two" size would be mandatory if we computed a FFT of all the points,
  // but to save bytes in this demo, we only compute a standard DFT. So this padding is finally only used only to add a nicer precision.
  // For example the built-in "JS1K" logo contains 33 points, in order to generate 64 gears.
  // It could have used less points, but it would look pretty bad with only 32 circles. You can see how bad by pressing "down" 32 times.
  for (b.bgColor = i = D = T = 0; P.length > 2 ** (Math.log2(P.length) | 0); i += 2)
    P.splice(i + 1, 0, [(P[i][0] + P[i + 1][0]) / 2, (P[i][1] + P[i + 1][1]) / 2]);

  // Compute the DFT of P.
  // This is black magic inspired by Paul Bourke's C++ code.
  _ = [];
  for (i in P) {
      _[i] = [0, 0];
      for (k in P)
          
          // Perform complex rotations or something like that?
          _[i][0] += (P[k][0] * Math.cos(k * -2 * Math.PI * i / P.length) - P[k][1] * Math.sin(k * -2 * Math.PI * i / P.length)),
          _[i][1] += (P[k][0] * Math.sin(k * -2 * Math.PI * i / P.length) + P[k][1] * Math.cos(k * -2 * Math.PI * i / P.length));
  }
  
  // Anyway, now we have the Fourier transform of the points computed and stored in P.
  P = _;

  // If P is not empty:
  if(P.length)
    
    // Compute the sizes and positions of the gears and place the values in G based on the DFT we just computed, converted to polar coordinates.
    for (I = P.length, G = []; I--;)

      G.push(
        [
          // Angle offset of the gear (based on the position of the current gear).
          I + P.length / 2 - P.length,
          
          // Radius of the gear (based on the magnitude of the current Fourier coefficient).
          Math.hypot(P[(I + P.length / 2) % P.length][0], P[(I + P.length / 2) % P.length][1]) / P.length,

          // Frequency of the gear (based of the frequency of the current Fourier coefficient).
          Math.atan2(P[(I + P.length / 2) % P.length][1], P[(I + P.length / 2) % P.length][0])
        ]
      );
  
  // Sort all the gears from the biggest to the smallest.
  // This is not mandatory (the gears can be in any order), but it looks better if we do it.
  G.sort((i, B) => B[1] - i[1]);
  
  // Set Q to the position of the last value of P to draw a path as precise as possible by default. 
  Q = P.length - 1
};

// Call f() on load to compute the gear of the "JS1K" pattern.
f();

// Run the drawing loop (every 9 ms):
setInterval(
e => {
  
  // Increase the time counter (T) very slowly, to allow one complete cycle to take about 1000 frames.
  T += .007;
  
  // Reset the canvas (a) and the vars U, V and g (center of the current gear and gear counter).
  a.width ^= U = V = g = 0;
  
  // Place the origin of the canvas at the center of the screen.
  c.translate(a.width / 2, a.height / 2);
  
  // Set the line color in white.
  c.strokeStyle = `#fff`;
  
  // Draw each point of p as a tiny circle.
  for (i of p)
    c.beginPath(),
    c.arc(i[0], i[1], 1, 0, 7),
    c.stroke();
    
  // Draw each gear as a circle, and draw a line between the center of each gear (U, V) and the center of the next gear (new values of U, V).
  for (i of G){
    c.beginPath();
    c.arc(U, V, i[1], 0, 7);
    c.moveTo(U, V);
    U += i[1] * Math.cos(i[0] * T + i[2]);
    V += i[1] * Math.sin(i[0] * T + i[2]);
    c.lineTo(U, V);
    
    // The g'th gear is actually traced in white, only if g is lower than the limit defined in Q.
    g <= Q && c.stroke();
      
    // Prepare the array of points traced by the g'th gear (Z[g]) if it has been erased by f() earlier.
    Z[g] = Z[g] || [];
    
    // Add U and V to Z[g], only if less than 999 points have been stored already.
    // (after ~999 points, the epicycloid loops and new points overlap the old ones, so we avoid storing / drawing them to increase the CPU performances).
    Z[g].length < 999 && Z[g].push([U,V]);
    
    g++
  }

  // Draw the path of each gear (if it is allowed by the values of Q and D).
  // g is reused as a gear counter.
  g = 0;
  for (i of G){
    c.beginPath();
    
    // The lines have a width of 5px...
    c.lineWidth = 5,
    
    // ... and a HSL color with a hue equal to "(Q - g) * 9".
    // The closing parenthesis of hsl() is not mandatory.
    c.strokeStyle = `hsl(${(Q-g)*9},50%,50%`,
    
    c.moveTo(Z[g][0], Z[g][1]);
    
    for(j of Z[g])
      
      // Only draw the g'th path if g is equal to the last gear of G, or equal to Q (if Q has a lower value than the last gear).
      // Also, if D is set, draw intermediate lines every 8 gears (gear 0 not included).
      (g == Math.min(Q, P.length - 1) || D && g && g <= Q && g % 8 < 1) && c.lineTo(j[0], j[1]);
      
    c.stroke();
    
    g++
  }
},
9)