@main def d2p2(args: String*): Unit =

  val inc = (x: Int, y: Int) => 1 <= (x - y) && (x - y) <= 3
  val dec = (x: Int, y: Int) => -1 >= (x - y) && (x - y) >= -3

  def isSafe(ls: List[Int], cond: (Int, Int) => Boolean): Boolean =
    def aux(ls: List[Int], hist: (Int, Int), life: Boolean): Boolean =
      (ls, hist) match
        case (hd :: tl, (pp, p)) if cond(p, hd) => aux(tl, (p, hd), life)
        case (hd :: tl, (pp, p)) if !cond(p, hd) && !life => false
        case (hd :: tl, (pp, p)) if !cond(p, hd) =>
          aux(tl, (pp, p), false) || aux(ls, (pp, pp), false)
        case _ => true

    ls match
      case a :: b :: c => aux(b :: c, (a, a), true) || aux(c, (b, b), false)
      case _           => true // short lists will always be satisfiable

  println(
    scala.io.Source
      .fromFile(if args.length > 0 then "d.in" else "sample.in")
      .getLines
      .map(_.split("\\s+").map(_.toInt).toList)
      .count(ls => isSafe(ls, inc) || isSafe(ls, dec))
  )
