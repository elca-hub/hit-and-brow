import random

ans_list = [] # 正解の記号が入ってるリスト

ans_range = 4

symbol_list = ["a", "b", "c", "d", "e", "f"]

for i in range(ans_range):
	ans_list.append(symbol_list[random.randint(0, ans_range - 1)])


is_2p = False

print("Hit And Blow")
print("記号はa, b, c, d, e, fのいずれかです。")

def check_user_input(user_input, ans_lenge, symbol_list):
		if len(user_input) != ans_lenge:
			return False
		
		for i in range(len(user_input)):
			if user_input[i] not in symbol_list:
				return False
		
		return True


def hit_and_blow(user_input, ans_list):
	hit_count = 0
	blow_count = 0
	for i in range(len(user_input)):
		if user_input[i] == ans_list[i]:
			hit_count += 1
			continue

		if user_input[i] in ans_list:
			blow_count += 1
	
	return hit_count, blow_count

while True:
	user_input = ""
	while True:
		user_input = input(("1P" if not is_2p else "2P") + "の番です :")
		
		if not check_user_input(user_input, ans_range, symbol_list):
			print("入力が不正です")
			continue
		break

	hit_count, blow_count = hit_and_blow(user_input, ans_list)

	print(hit_count, blow_count)

	if hit_count == ans_range:
		print(("1P" if not is_2p else "2P") + "の勝ちです！")
		print("正解 : " + user_input)
		break
	
	print("{}ヒット{}ブロー".format(hit_count, blow_count))

	is_2p = not is_2p
