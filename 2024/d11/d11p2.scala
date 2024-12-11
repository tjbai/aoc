import scala.collection.mutable.Map

@main def d11p2(args: String*): Unit =
  val line = scala.io.Source
    .fromFile(if args.length > 0 then "d.in" else "sample.in")
    .getLines
    .next
    .split(" ")
    .map(_.toLong)

  var cache = Map[(Long, Long), Long]()
  def expand(stone: Long, depth: Int): Long =
    cache.getOrElseUpdate(
      (stone, depth), {
        if depth == 0 then 1
        else
          stone.toString match
            case "0" =>
              expand(1L, depth - 1)
            case s if s.length % 2 == 0 =>
              val (fh, bh) = s.splitAt(s.length / 2)
              expand(fh.toLong, depth - 1) + expand(bh.toLong, depth - 1)
            case _ =>
              expand(stone * 2024, depth - 1)
      }
    )

  println(line.map(expand(_, 75)).sum)
