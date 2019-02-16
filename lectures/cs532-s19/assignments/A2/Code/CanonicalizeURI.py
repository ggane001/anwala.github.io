{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "www.forbes.com/sites/geraldfenech/2019/01/15/integrating-art-gaming-and-commerce-through-blockchain/\n",
      "www.youtube.com/watch/v=kTsEbKFD4ZU&feature=youtu.be\n",
      "www.forbes.com/sites/geraldfenech/2019/01/15/integrating-art-gaming-and-commerce-through-blockchain/\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "from urllib.parse import urlparse\n",
    "\n",
    "def canonicalizeURI(uri):\n",
    "\n",
    "    uri = uri.strip()\n",
    "    if( len(uri) == 0 ):\n",
    "        return ''\n",
    "\n",
    "    exceptionDomains = ['www.youtube.com']\n",
    "\n",
    "    try:\n",
    "        scheme, netloc, path, params, query, fragment = urlparse( uri )\n",
    "        netloc = netloc.strip()\n",
    "        path = path.strip()\n",
    "        optionalQuery = ''\n",
    "\n",
    "        if( len(path) != 0 ):\n",
    "            if( path[-1] != '/' ):\n",
    "                path = path + '/'\n",
    "\n",
    "        if( netloc in exceptionDomains ):\n",
    "            optionalQuery = query.strip()\n",
    "\n",
    "        return netloc + path + optionalQuery\n",
    "    except:\n",
    "        print('Error uri:', uri)\n",
    "\n",
    "    return ''\n",
    "\n",
    "uri0 = 'https://www.forbes.com/sites/geraldfenech/2019/01/15/integrating-art-gaming-and-commerce-through-blockchain/#2ac9b72d56d3'\n",
    "uri1 = 'https://www.youtube.com/watch?v=kTsEbKFD4ZU&feature=youtu.be'\n",
    "uri2 = 'https://www.forbes.com/sites/geraldfenech/2019/01/15/integrating-art-gaming-and-commerce-through-blockchain/#2ac9b72d56d3?key=val&key2=val'\n",
    "\n",
    "#uri0 and uri1 are different\n",
    "print(canonicalizeURI(uri0))\n",
    "print(canonicalizeURI(uri1))\n",
    "print(canonicalizeURI(uri2))\n",
    "print( canonicalizeURI(uri0) == canonicalizeURI(uri1) )\n",
    "#uri0 and uri2 are too similar\n",
    "print( canonicalizeURI(uri0) == canonicalizeURI(uri2) )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
