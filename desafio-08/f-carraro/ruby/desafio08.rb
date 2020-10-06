def simp(c,d)
  return c if d==1
  return 1 if c==d
  return 'ERR' if d==0
  g = c.gcd(d)
  i = c/d
  i == 0 ? s='' : s=i.to_s + ' '
  return s + "#{(c-i*d)/g}/#{d/g}"
end

ARGF.each_line do |line|
  a,b = line.split('/')
  puts simp(a.to_i, b ? b.to_i : 1)
end
