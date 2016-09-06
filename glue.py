import re

from collections import defaultdict

global method_dict
# initialize the dictionary
method_dict = {'getContentResolver().deleteRecord(mUri, null, null)' : 'getContentResolver().delete(mUri, null, null)'}

# For each given answer by the user
def glue_answer(answer_block):
	#open the file
	filein = open("NoteEditor.java")
	#read it
	src = Template(filein.read())
	#do the substitution
	result = src.substitute(bind_method(answer_block))
	return result

# Bind the answer to the real Android method
def bind_method(answer):
	answ = ""
	m_keys = list(method_dict.keys())
	for l, m in enumerate(m_keys):
		if (answer.find(m_keys[l])):
			answ = answer.replace(m_keys[l], method_dict.get(m_keys[l]))
			break
		else:
			answ = answer
	return answ