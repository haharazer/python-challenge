def trans_letter(letter):
	if ord(letter) >122 or ord(letter) < 96:
		return letter
	trans_ascii = ord(letter) + 2
	if trans_ascii > 122:
		trans_ascii -= 26
	return chr(trans_ascii)

def trans_string(s):
	ret = ''
	for l in s:
		ret += trans_letter(l)
	return ret
	
ori_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print trans_string(ori_str)

print trans_string('map')