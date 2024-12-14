@main def d14p2(args: String*): Unit =
  val (rows, cols) = (103, 101)
  val pattern = "p=(\\d+),(\\d+) v=(-?\\d+),(-?\\d+)".r

  def locAt(p: (Int, Int), v: (Int, Int), t: Int): (Int, Int) =
    t match
      case 0 => p
      case _ => locAt(((p._1 + v._1 + rows) % rows, (p._2 + v._2 + cols) % cols), v, t - 1)

  def arrange(ps: Seq[(Int, Int)]): Unit = ()

  val robots = scala.io.Source
    .fromFile(if args.length > 0 then "d.in" else "sample.in")
    .getLines
    .map { case pattern(px, py, vx, vy) => locAt((py.toInt, px.toInt), (vy.toInt, vx.toInt), 100) }
    .toSeq
