def designerPdfViewer(h, word):
  max_height = 0
  for i in word:
    if max_height < h[ord(i)-ord("a")]:
      max_height = h[ord(i)-ord("a")]

  return len(word) * max_height

print(designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], "abc"))
