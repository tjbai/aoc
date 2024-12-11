@main def d6p1(args: String*): Unit =

  val map = scala.io.Source
    .fromFile(if args.length > 0 then "d.in" else "sample.in")
    .getLines
    .toSeq

  var seen = Set[(Int, Int)]()
  val (rows, cols) = (map.length, map(0).length)
  val dirs = IArray((-1, 0), (0, 1), (1, 0), (0, -1))

  val start = (for
    r <- 0 until rows
    c <- 0 until cols
    if map(r)(c) == '^'
  yield (r, c))(0)

  def step(r: Int, c: Int, d: Int): Unit =
    seen = seen + ((r, c))
    val (nr, nc) = (r + dirs(d)(0), c + dirs(d)(1))
    (nr, nc) match
      case _ if nr < 0 || nc < 0 || nr >= rows || nc >= cols => ()
      case _ if map(nr)(nc) == '#' => step(r, c, (d + 1) % 4)
      case _ => step(nr, nc, d)

  step(start(0), start(1), 0)
  println(seen.size)
