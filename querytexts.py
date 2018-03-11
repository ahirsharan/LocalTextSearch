import buildindex
import re
import glob
import json
from datetime import datetime
from collections import OrderedDict
#NEED TO TEST MORE.

#input = [file1, file2, ...]
#res = {word: {filename: {pos1, pos2}, ...}, ...}
class Query:

	def __init__(self, filenames):
		self.filenames = filenames
		self.index = buildindex.BuildIndex(self.filenames)
		self.invertedIndex = self.index.totalIndex
		self.regularIndex = self.index.regdex


	def one_word_query(self, word):
		# pattern = re.compile('[\W_]+')
		# word = pattern.sub(' ',word)
		#print(self.invertedIndex)
		if word in self.invertedIndex.keys():
			#return self.rankResults([filename for filename in self.invertedIndex[word]], word)
			r = self.invertedIndex[word]
			return r
		else:
			return None

	def free_text_query(self, string):
		# pattern = re.compile('[\W_]+')
		# string = pattern.sub(' ',string)
		result = []
		for word in string.split():
			result.append(self.one_word_query(word))
		return result
		# result = []
		# for word in string.split():
		# 	result += self.one_word_query(word)
		# return self.rankResults(list(set(result)), string)


	#inputs = 'query string', {word: {filename: [pos1, pos2, ...], ...}, ...}
	#inter = {filename: [pos1, pos2]}
	def phrase_query(self, string):
		pattern = re.compile('[\W_]+')
		string = pattern.sub(' ',string)
		listOfLists, result = [],[]
		for word in string.split():
			listOfLists.append(self.one_word_query(word))
		setted = set(listOfLists[0]).intersection(*listOfLists)
		for filename in setted:
			temp = []
			for word in string.split():
				temp.append(self.invertedIndex[word][filename][:])
			for i in range(len(temp)):
				for ind in range(len(temp[i])):
					temp[i][ind] -= i
			if set(temp[0]).intersection(*temp):
				result.append(filename)
		return self.rankResults(result, string)

	def make_vectors(self, documents):
		vecs = {}
		for doc in documents:
			docVec = [0]*len(self.index.getUniques())
			for ind, term in enumerate(self.index.getUniques()):
				docVec[ind] = self.index.generateScore(term, doc)
			vecs[doc] = docVec
		return vecs


	def query_vec(self, query):
		pattern = re.compile('[\W_]+')
		query = pattern.sub(' ',query)
		queryls = query.split()
		queryVec = [0]*len(queryls)
		index = 0
		for ind, word in enumerate(queryls):
			queryVec[index] = self.queryFreq(word, query)
			index += 1
		queryidf = [self.index.idf[word] for word in self.index.getUniques()]
		magnitude = pow(sum(map(lambda x: x**2, queryVec)),.5)
		freq = self.termfreq(self.index.getUniques(), query)
		#print('THIS IS THE FREQ')
		tf = [x/magnitude for x in freq]
		final = [tf[i]*queryidf[i] for i in range(len(self.index.getUniques()))]
		#print(len([x for x in queryidf if x != 0]) - len(queryidf))
		return final

	def queryFreq(self, term, query):
		count = 0
		#print(query)
		#print(query.split())
		for word in query.split():
			if word == term:
				count += 1
		return count

	def termfreq(self, terms, query):
		temp = [0]*len(terms)
		for i,term in enumerate(terms):
			temp[i] = self.queryFreq(term, query)
			#print(self.queryFreq(term, query))
		return temp

	def dotProduct(self, doc1, doc2):
		if len(doc1) != len(doc2):
			return 0
		return sum([x*y for x,y in zip(doc1, doc2)])

	def rankResults(self, resultDocs, query):
		vectors = self.make_vectors(resultDocs)
		#print(vectors)
		queryVec = self.query_vec(query)
		#print(queryVec)
		results = [[self.dotProduct(vectors[result], queryVec), result] for result in resultDocs]
		#print(results)
		results.sort(key=lambda x: x[0])
		#print(results)
		results = [x[1] for x in results]
		return results

def Build(haystack):
	b = []
	c=0
	for line in block:
		pattern = re.compile('[\W_]+')
		line = pattern.sub(' ',line)
		word_count = len(line.split())
		if(c == 0):
			b.append(word_count)
			c=1
		else:
			b.append(word_count + b[-1])
	return b

# main
r = []
CRED = '\033[42m'
CRED22 = '\033[104m'
CRED2 = '\033[0m'
startTime = datetime.now()
for name in glob.glob('*.txt'):
	r.append(name)
q = Query(r)
print (CRED + "TIME TO INDEX = " + CRED2)
ti = datetime.now() - startTime
print (ti)
pat = "a"
while (pat != "!q"):
	print()
	pat = input(CRED + "ENTER THE SEARCH QUERY: " + CRED2)
	print()
	if(pat != "!q"):
		print()
		res = q.free_text_query(pat)
		#print(json.dumps(res, indent = 4)
		if(res != None):
			c=0
			se = set(res[0]).intersection(*res)


			# dictionary response
			# print("PARTS OF PATTERN FOUND IN: ")
			# for word in pat.split():
			# 	print(word)
			# 	print()
			# 	print(json.dumps(res[c], indent = 4, sort_keys=True))
			# 	print()
			# 	c += 1

			print(CRED + "COMPLETE PATTERN FOUND IN : " + CRED2)
			print()
			max = 0
			for keys in se:
				print(keys)
			a = pat.split()
			print()
			print(CRED + "SEPERATE WORDS FOUND IN:" + CRED2)
			print()
			c = 0
			for terms in res:
				print(CRED + "WORD IS:" + CRED2)
				print("----------"),
				print(a[c])
				print("----------")
				print()

				rank = dict()
				for keys in terms.keys():
					length = len(terms[keys])
					if length in rank.keys():
						rank[length].append(keys)
					else:
						rank[length] = []
						rank[length].append(keys)

				# print(rank)
				qw = sorted(rank)

				# qw has the index in x of documents in increasing
				# order of frequency of query
				for n in qw:
					for x in rank[n]:
						#x is a filename
						print(CRED + "FILE NAME:" + CRED2)
						print("*******")
						print(x)
						print("*******")
						# WORD NUMBER IN FILE
						# print("WORD NUMBER IN THE FILE: ")
						# print()
						# print(terms[x])
						# print()

						#line NUMBER
						with open(x, 'r') as myfile:
							block=myfile.readlines()
						word_data = Build(block)
						print(CRED + "FOUND AT LINE NUMBER:" + CRED2)
						for y in terms[x]:
							line_number = 0
							for z in word_data:
								if(z >= y):
									print(line_number + 1)
									break
								else:
									line_number += 1

				print()
				pat_search = q.phrase_query(pat)
				print(CRED + "RESULT FOUND IN INCREASING ORDER OF RELEVANCE IN: " + CRED2)
				print()
				for item in pat_search:
					print(item)


				c += 1
