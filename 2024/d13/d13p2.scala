@main def d13p2(args: String*): Unit =
  def isInt(d: Double, tol: Double = 1e-10): Option[Long] =
    if math.abs(d - d.round) <= tol then Some(d.round.toLong) else None

  val cases = scala.io.Source
    .fromFile(if args.length > 0 then "d.in" else "sample.in")
    .mkString
    .split("\n\n")

  println(cases.map {
    case s"Button A: X+${_a}, Y+${_c}\nButton B: X+${_b}, Y+${_d}\nPrize: X=${_x}, Y=${_y}" =>
      val (a, b, c, d, x, y) =
        (_a.toDouble, _b.toDouble, _c.toDouble, _d.toDouble, _x.toDouble + 1e13, _y.toDouble + 1e13)

      // not gonna take credit for this
      // tried gaussian elimination but ran into stability issues
      val det = a * d - b * c
      val e = (x * d - b * y) / det
      val f = (a * y - c * x) / det

      (isInt(e), isInt(f)) match
        case (Some(e), Some(f)) => 3 * e + f
        case _ => 0
  }.sum)
