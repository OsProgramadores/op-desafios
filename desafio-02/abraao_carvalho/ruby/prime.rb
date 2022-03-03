first = 1
last = 1000

puts 'Prime numbers: ' + first.to_s + ' a ' + last.to_s + ':'

for i in first..last do
	k = 0
	for j in 2..i
		if i % j == 0 then
			k = k + 1
		end
	end
	if k == 1 then
		puts i
	end
end