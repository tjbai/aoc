import scala.collection.mutable

@main def d17p1(args: String*): Unit =
  val lines = scala.io.Source
    .fromFile(if args.length > 0 then "d.in" else "sample.in")
    .mkString

  var Array(registers, _program) = lines.split("\n\n")
  var Array(a, b, c) = registers.split("\n").map(_.split(": ")(1).toInt)
  var program = _program.strip.split(": ")(1).split(",").map(_.toInt)

  var p = 0
  var out = mutable.ArrayBuffer[Int]()

  while p < program.length do
    val op = program(p)
    val literal = program(p + 1)
    val combo = if literal <= 3 then literal else Array(a, b, c)(literal - 4)

    op match
      case 0 => a >>= combo
      case 1 => b ^= literal
      case 2 => b = combo & 7
      case 3 => if a != 0 then p = literal - 2
      case 4 => b ^= c
      case 5 => out.append(combo & 7)
      case 6 => b = a >> combo
      case 7 => c = a >> combo
    p += 2

  println(out.mkString(","))
