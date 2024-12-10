@main def d10p2(args: String*): Unit =
  val lines = scala.io.Source
    .fromFile(if args.length > 0 then "d.in" else "sample.in")
    .getLines
    .map(_.map(_ - '0'))
    .toIndexedSeq

  val (rows, cols) = (lines.length, lines(0).length)

  def search(r: Int, c: Int, prev: Int, seen: Set[(Int, Int)]): Int =
    if seen((r, c))
      || r < 0 || c < 0 || r >= rows || c >= cols
      || lines(r)(c) != prev + 1
    then 0
    else if lines(r)(c) == 9 then 1
    else
      search(r + 1, c, prev + 1, seen + ((r, c)))
        + search(r, c + 1, prev + 1, seen + ((r, c)))
        + search(r - 1, c, prev + 1, seen + ((r, c)))
        + search(r, c - 1, prev + 1, seen + ((r, c)))

  println((for
    r <- 0 until rows
    c <- 0 until cols
    if lines(r)(c) == 0
  yield search(r, c, -1, Set())).sum)
