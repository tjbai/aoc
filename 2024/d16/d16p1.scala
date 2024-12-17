import scala.collection.mutable

@main def d16p1(args: String*): Unit =
  val lines = scala.io.Source
    .fromFile(if args.length > 0 then "d.in" else "sample.in")
    .getLines
    .toArray

  val (rows, cols) = (lines.length, lines(0).length)
  val (dirL, dirR, dirU, dirD) = (0, 1, 2, 3) // poor man's enum

  val (sr, sc) = (for
    r <- 0 until rows
    c <- 0 until cols
    if lines(r)(c) == 'S'
  yield (r, c))(0)

  var seen = mutable.Set[(Int, Int, Int)]()
  var pq = mutable.PriorityQueue((0, sr, sc, dirR)).reverse
  while pq.length > 0
  do
    var (p, r, c, d) = pq.dequeue
    if lines(r)(c) != '#' && !seen((r, c, d)) && r >= 0 && c >= 0 && r < rows && c < cols then
      seen += ((r, c, d))
      if lines(r)(c) == 'E' then println(p)
      for (dr, dc, nd) <- Seq((0, -1, dirL), (0, 1, dirR), (-1, 0, dirU), (1, 0, dirD))
      do pq += ((p + 1 + (if nd != d then 1000 else 0), r + dr, c + dc, nd))
