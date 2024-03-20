def decode(message_file):
  number_word_map = {}
  with open(message_file, 'r') as file:
    for line in file:
      number, word = line.strip().split(' ', 1)
      number_word_map[int(number)] = word

  key_positions = []
  n = 1
  while n in number_word_map:
    key_positions.append(n)
    n = len(key_positions) + 1
    n = n * (n + 1) // 2
  message_words = [number_word_map[pos] for pos in key_positions if pos in number_word_map]
  message = ' '.join(message_words)
  return message

if __name__ == "__main__":
    decoded_message = decode('coding_qual_input.txt')  # Replace 'message.txt' with your actual file name if different
    print(decoded_message)

