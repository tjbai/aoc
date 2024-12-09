@main def d8p1(args: String*): Unit =
  val lines = scala.io.Source
    .fromFile(if args.length > 0 then "d.in" else "sample.in")
    .getLines
    .toSeq

  val (rows, cols) = (lines.length, lines(0).length)

  def getAntinodes(v: Seq[(Int, Int)]): Iterator[(Int, Int)] =
    v.combinations(2)
      .flatMap { case Seq((r1: Int, c1: Int), (r2: Int, c2: Int)) =>
        val (dr, dc) = (r2 - r1, c2 - c1)
        Seq((r1 - dr, c1 - dc), (r2 + dr, c2 + dc))
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
      .filter((r, c) => r >= 0 && c >= 0 && r < rows && c < cols)
      .size
  )
