object D1P2:
  @main def p2(args: String*): Unit =
    val ls = scala.io.Source
      .fromFile(if args.length > 0 then "d.in" else "sample.in")
      .getLines
      .map(_.split("\\s+").map(_.toInt))
      .toList

    val freq = ls
      .map(_(1))
      .groupBy(identity)
      .mapValues(_.length)

    println(ls.map(x => x(0) * freq.getOrElse(x(0), 0)).sum)
