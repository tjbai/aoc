@main def d3p1(args: String*): Unit =
  enum Token:
    case Mul, Lparen, Rparen, Sep, Empty
    case Num(value: Int)

  extension (source: Seq[Char])
    def tokenize: List[Token] =
      import Token.*
      def aux(ls: Seq[Char], tokens: List[Token], num: List[Char]): List[Token] =
        (ls, num) match
          case (d :: tl, _) if d.isDigit => aux(tl, tokens, d :: num)
          case (d :: tl, hd :: _) => aux(d :: tl, Num(num.reverse.mkString.toInt) :: tokens, List())
          case ('(' :: tl, _)     => aux(tl, Lparen :: tokens, num)
          case (')' :: tl, _)     => aux(tl, Rparen :: tokens, num)
          case ('m' :: 'u' :: 'l' :: tl, _) => aux(tl, Mul :: tokens, num)
          case (',' :: tl, _)               => aux(tl, Sep :: tokens, num)
          case (_ :: tl, _)                 => aux(tl, Empty :: tokens, num)
          case (_, _)                       => tokens.reverse
      aux(source, List(), List())

  extension (tokens: List[Token])
    def eval: Int =
      import Token.*
      def aux(tokens: List[Token], acc: Int): Int = tokens match
        case Mul :: Lparen :: Num(a) :: Sep :: Num(b) :: Rparen :: tl => aux(tl, acc + a * b)
        case _ :: tl                                                  => aux(tl, acc)
        case _                                                        => acc
      aux(tokens, 0)

  println(
    scala.io.Source
      .fromFile(if args.length > 0 then "d.in" else "sample.in")
      .toSeq
      .tokenize
      .eval
  )
