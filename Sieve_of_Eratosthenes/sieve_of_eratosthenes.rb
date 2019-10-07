#cerner_2^5_2019
def sieve_of_eratosthenes(list)
  num_iters = Math.sqrt(list[-1]).to_i
  hashed = Hash[list.collect { |x| [x, true] }]
  hashed.each_with_index do |(key, value), index|
    break if index >= num_iters
    if value == true
      i = 0
      while key**2 + key*i <= hashed.length + 1 do
        x = key**2 + key*i
        hashed[x] = false
        i += 1
      end
    end
  end
  puts hashed.select { |_, v| v == true }.keys
end

puts 'Enter a number: '
n = gets.to_i
list = [*2..n]
sieve_of_eratosthenes(list)