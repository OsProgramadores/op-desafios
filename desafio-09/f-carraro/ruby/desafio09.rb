def base(from,to,ns)
	c = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
	return '???' unless (2..62)===from && (2..62)===to && ns.chars.all?{|e| c[0..from-1].include?(e)}
	n = ns.reverse.chars.each_with_index.reduce(0){|r,(a,i)| r+c.index(a)*from**i}
	return '0'   if n == 0
	return '???' if n > 591222134364399413463902591994678504204696392694759423
	sol = ''
	while n > 0
		sol = c[n%to] + sol
		n /= to
	end
	return sol
end

ARGF.each_line do |line|
  f,t,ns = line.split
  puts base(f.to_i,t.to_i,ns)
end
