import streamlit as st
st.title("Book library📚")
#===========Books===============
ifcc'books' not in st.sessions_state:
st.session_state.books = []
#===============ADD=============
st.header("ADD a book and its price , author , title ")
tite = st.text_input("Title?")
author = st.text_input("Author of the book")
price = st.number_input("price", min_value = 0 )
if st.button("Add the book ?"):
  book = {"title": title,
          "author":author,
          "price":price}
  st.session_state.books.append(book)
  st.success("The book has been added ")
#============APP=============
if st.button("Check"):
  if len(st.session_state.books) == 0:
    st.write("No book has been added ")
  else:
    for book in st.session_state.books:
      st.write("Ttitle:", book["title"])
      st.write("author:", book["author"])
      st.write("price:", book["price"])
      st.write("---------------------------")
#=================Author search====================
st.header("serch by author")
s_author = st.text_input("name of author")
if st.button("search"):
  found = False
  for book in st.session_state.books:
    if book["author"] == s_author:
      st.write(book)
      found = True
 if not found :
   st.write("No such author")
#==================search for title============
st.header("search by title")
s_title = st.text_input("input your title')
if st.button("search by title"):
    found = False
  for book in st.session_state.books:
    if book["title"] == s_title:
      st.write(book)
      found = True
 if not found :
   st.write("No such title") 
#======================Cheapest book============
if st.button("search for the cheapest book"):
  if len(st.session_state.books) == 0 :
    st.write("No books")
  else:
    cheapest = st.session_state.books[0]




                        





  







