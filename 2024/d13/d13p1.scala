import scala.collection.mutable

@main def d13p1(args: String*): Unit =
  val cases = scala.io.Source
    .fromFile(if args.length > 0 then "d.in" else "sample.in")
    .mkString
    .split("\n\n")

  def cheapest(
      a: (Int, Int),
      b: (Int, Int),
      t: (Int, Int),
      cache: mutable.Map[(Int, Int), Int]
  ): Int =
    cache.getOrElseUpdate(
      t, {
        t match
          case (0, 0) => 0
          case (xt, yt) if xt < 0 || yt < 0 => 600
          case (xt, yt) =>
            math.min(
              3 + cheapest(a, b, (xt - a._1, yt - a._2), cache),
              1 + cheapest(a, b, (xt - b._1, yt - b._2), cache)
            )
      }
    )

  println(
    cases.map {
      case s"Button A: X+${xa}, Y+${ya}\nButton B: X+${xb}, Y+${yb}\nPrize: X=${xt}, Y=${yt}" =>
        var cache = mutable.Map[(Int, Int), Int]()
        cheapest((xa.toInt, ya.toInt), (xb.toInt, yb.toInt), (xt.toInt, yt.toInt), cache) match
          case res if res >= 600 => 0
          case res => res
    }.sum
  )
