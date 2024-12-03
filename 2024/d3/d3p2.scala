@main def d3p2(args: String*): Unit =
  enum Token:
    case Mul, Lp, Rp, Sep, Empty, Do, Dont
    case Num(value: Int)

  extension (source: Seq[Char])
    def tokenize: List[Token] =
      import Token.*
      def aux(ls: Seq[Char], tokens: List[Token], num: List[Char]): List[Token] =
        (ls, num) match
          case (d :: tl, _) if d.isDigit => aux(tl, tokens, d :: num)
          case (d :: tl, hd :: _) => aux(d :: tl, Num(num.reverse.mkString.toInt) :: tokens, List())
          case ('(' :: tl, _)     => aux(tl, Lp :: tokens, num)
          case (')' :: tl, _)     => aux(tl, Rp :: tokens, num)
          case ('m' :: 'u' :: 'l' :: tl, _)                => aux(tl, Mul :: tokens, num)
          case ('d' :: 'o' :: 'n' :: '\'' :: 't' :: tl, _) => aux(tl, Dont :: tokens, num)
          case ('d' :: 'o' :: tl, _)                       => aux(tl, Do :: tokens, num)
          case (',' :: tl, _)                              => aux(tl, Sep :: tokens, num)
          case (_ :: tl, _)                                => aux(tl, Empty :: tokens, num)
          case (_, _)                                      => tokens.reverse
      aux(source, List(), List())

  extension (tokens: List[Token])
    def eval: Int =
      import Token.*
      def aux(tokens: List[Token], acc: Int, on: Boolean): Int = tokens match
        case Mul :: Lp :: Num(a) :: Sep :: Num(b) :: Rp :: tl if on => aux(tl, acc + a * b, on)
        case Do :: Lp :: Rp :: tl                                   => aux(tl, acc, true)
        case Dont :: Lp :: Rp :: tl                                 => aux(tl, acc, false)
        case _ :: tl                                                => aux(tl, acc, on)
        case _                                                      => acc
      aux(tokens, 0, true)

  println(
    scala.io.Source
      .fromFile(if args.length > 0 then "d.in" else "sample.in")
      .toSeq
      .tokenize
      .eval
  )
