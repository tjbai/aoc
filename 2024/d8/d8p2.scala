@main def d8p2(args: String*): Unit =
  val lines = scala.io.Source
    .fromFile(if args.length > 0 then "d.in" else "sample.in")
    .getLines
    .toSeq

  val (rows, cols) = (lines.length, lines(0).length)

  def getAntinodes(points: Seq[(Int, Int)]): Iterator[(Int, Int)] =
    def iter(r: Int, c: Int, dr: Int, dc: Int): Iterator[(Int, Int)] =
      Iterator.unfold((r, c)) {
        case (r, c) if r < 0 || c < 0 || r >= rows || c >= cols => None
        case (r, c) => Some((r, c), (r + dr, c + dc))
      }

    points
      .combinations(2)
      .flatMap { case Seq((r1: Int, c1: Int), (r2: Int, c2: Int)) =>
        val (dr, dc) = (r2 - r1, c2 - c1)
        iter(r2, c2, dr, dc) ++ iter(r1, c1, -dr, -dc)
      }

  println(
    (for
      r <- 0 until rows
      c <- 0 until cols
      if lines(r)(c) != '.'
    yield (r, c, lines(r)(c)))
      .groupBy(_(2))
      .mapValues(_.map((r, c, _) => (r, c)))
      .values
      .flatMap(getAntinodes)
      .toSet
      .size
  )
