class IO
  def tac
    b = [64*1024,size].min
    seek -b, SEEK_END
    buf = ""
    while pos > b
      while buf.count("\n") <= 1
        break if pos < b
        buf = read(b) + buf
        seek 2*-b, SEEK_CUR
      end
      buf,*rest = buf.lines
      $stdout.puts rest.reverse
    end
    left = pos
    seek -left, SEEK_CUR
    buf = read(left+b) + buf
    $stdout.puts buf.lines.reverse
  end
end

File.open(ARGV[0]).tac
