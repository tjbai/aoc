object D1P1:
  @main def p1(args: String*): Unit =
    var input = scala.io.Source
      .fromFile(if args.length > 0 then "d.in" else "sample.in")
      .getLines
      .toList

    val ls1 = input.map(_.split("\\s+")(0).toInt).sorted
    val ls2 = input.map(_.split("\\s+")(1).toInt).sorted

    println(ls1.zip(ls2).map((a, b) => (a - b)).map(_.abs).sum)
