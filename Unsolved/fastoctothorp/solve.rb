#!/usr/bin/env ruby
require 'ruby-xxhash'

hashes = File.read('./hashes.txt')

def do_hash(text, seed) 
	return XXhash.xxh64(text, seed)
end

char_count = 6
charset = [*:a..:z]

for seed in (10000-1).downto(0)
	charset.permutation(char_count) do |a|
		text = a.join
		myhash = do_hash(text, seed).to_s

		if hashes.include? myhash then
			puts('WPI{' + text + seed.to_s + '}')
			exit
		end
		puts 'Tried' + text
	end
	puts 'Tried' + seed.to_s
end
