const std = @import("std");

// Returns true if the given number is a palindrome, false otherwise
pub fn is_palindrome(num: u64) bool {
    // Create a copy of the number
    var copy = num;

    // Initialize the reversed number to 0
    var reversed: u64 = 0;

    // Loop until there are no more digits to reverse
    while (copy > 0) {
        // Add the last digit of the number to the reversed number
        reversed = (reversed * 10) + (copy % 10);

        // Remove the last digit from the number
        copy /= 10;
    }

    // Return true if the number is the same forwards and backwards
    return num == reversed;
}

pub fn main() void {
    pallindrome(1, 20);
    pallindrome(3000, 3010);
}

fn pallindrome(start: usize, end: usize) void {
    // Loop through each number between start and end (inclusive)
    var num = start;
    while (num < end) : (num += 1) {
        // If the number is a palindrome, print it
        if (is_palindrome(num)) {
            std.debug.print("{}", .{num});
            // skip comma ","
            if (num < end - num) std.debug.print(",", .{});
        }
    }
    std.debug.print(".\n", .{});
}
