enum Token:
  case Mul
  case LParen
  case RParen
  case Sep
  case Empty
  case Num(value: Int)
import Token.*

def tokenize(
    ls: Seq[Char],
    tokens: List[Token] = List(),
    num: List[Char] = List()
): List[Token] =
  (ls, num) match
    case (d :: tl, _) if d.isDigit => tokenize(tl, tokens, d :: num)
    case (d :: tl, hd :: _) if !d.isDigit =>
      val numTok = Num(num.reverse.mkString("").toInt)
      tokenize(d :: tl, numTok :: tokens, List())
    case ('(' :: tl, _)               => tokenize(tl, LParen :: tokens, num)
    case (')' :: tl, _)               => tokenize(tl, RParen :: tokens, num)
    case ('m' :: 'u' :: 'l' :: tl, _) => tokenize(tl, Mul :: tokens, num)
    case (',' :: tl, _)               => tokenize(tl, Sep :: tokens, num)
    case (_ :: tl, _)                 => tokenize(tl, Empty :: tokens, num)
    case (_, _)                       => tokens.reverse

def eval(tokens: List[Token], acc: Int = 0): Int =
  tokens match
    case Mul :: LParen :: Num(a) :: Sep :: Num(b) :: RParen :: tl => eval(tl, acc + a * b)
    case _ :: tl                                                  => eval(tl, acc)
    case _                                                        => acc

@main def d3p1(args: String*): Unit =
  val source = scala.io.Source
    .fromFile(if args.length > 0 then "d.in" else "sample.in")
    .toSeq

  // no pipelines hurts
  println(eval(tokenize(source)))
