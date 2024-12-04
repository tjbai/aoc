@main def d4p1(args: String*): Unit =
  val lines = scala.io.Source
    .fromFile(if args.length > 0 then "d.in" else "sample.in")
    .getLines
    .toArray

  val (targ, rows, cols) = ("XMAS", lines.length, lines(0).length)
  val dirs = List((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1))

  def search(r: Int, c: Int, dr: Int, dc: Int, char: Int = 0): Int =
    if char == 4 then 1
    else if r < 0 || c < 0 || r >= rows || c >= cols || lines(r)(c) != targ(char) then 0
    else search(r + dr, c + dc, dr, dc, char + 1)

  println((for
    r <- 0 until rows
    c <- 0 until cols
    (dr, dc) <- dirs
  yield search(r, c, dr, dc)).sum)
