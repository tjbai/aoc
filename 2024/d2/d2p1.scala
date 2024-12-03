@main def d2p1(args: String*): Unit =

  def isSafe(ls: Array[Int]): Boolean =
    val diffs = ls.zip(ls.tail).map(_ - _)
    diffs.forall(x => 1 <= x && x <= 3) || diffs.forall(x => -1 >= x && x >= -3)

  println(
    scala.io.Source
      .fromFile(if args.length > 0 then "d.in" else "sample.in")
      .getLines
      .map(_.split("\\s+").map(_.toInt))
      .count(isSafe)
  )
