@main def d4p2(args: String*): Unit =
  val lines = scala.io.Source
    .fromFile(if args.length > 0 then "d.in" else "sample.in")
    .getLines
    .toArray

  def X(r: Int, c: Int) =
    Seq(
      lines(r - 1)(c - 1),
      lines(r - 1)(c + 1),
      lines(r + 1)(c - 1),
      lines(r + 1)(c + 1)
    ).mkString match {
      case "MSMS" | "MMSS" | "SSMM" | "SMSM" => 1
      case _ => 0
    }

  println((for
    r <- 1 until lines.length - 1
    c <- 1 until lines(0).length - 1
    if lines(r)(c) == 'A'
  yield X(r, c)).sum)
