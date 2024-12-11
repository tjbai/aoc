@main def d11p1(args: String*): Unit =
  def update(stone: Long): Seq[Long] =
    stone.toString match
      case "0" => Seq(1L)
      case s if s.length % 2 == 0 =>
        val (fh, bh) = s.splitAt(s.length / 2)
        Seq(fh.toLong, bh.toLong)
      case _ => Seq(stone * 2024)

  val line = scala.io.Source
    .fromFile(if args.length > 0 then "d.in" else "sample.in")
    .getLines
    .next
    .split(" ")
    .map(_.toLong)

  val len = LazyList
    .iterate(line)(_.flatMap(update))
    .take(26)
    .last
    .length

  println(len)
