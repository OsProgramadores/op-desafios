const std = @import("std");
const math = std.math;

pub fn primos(n: usize) bool {
    var i = math.sqrt(n);
    while (i > 1) : (i -= 1) {
        if((n % i) == 0) {
            return false;
        }
    }
    return true;
}

pub fn main() void {
    const limit = 100000;
    var numbers :usize = 2;
    while (numbers < limit) : (numbers += 1){
        if(primos(numbers)){
            std.debug.print("{} is prime.\n",.{numbers});
        }
    }
}
