const oddCells = (n, m, indices) => {
  const [rows, cols] = [new Array(n).fill(0), new Array(m).fill(0)];
  for (const [ri, ci] of indices) [rows[ri]++, cols[ci]++];
  const rowOdds = rows.filter(n => 1 === n % 2).length;
  const rowEvens = rows.length - rowOdds;
  const colOdds = cols.filter(n => 1 === n % 2).length;
  const colEvens = cols.length - colOdds;
  return rowOdds * colEvens + rowEvens * colOdds;
};