| Python   | quick | reference | | |
|----------------------------|----------------------------|-------------------------------|------------------------|------------------------|
| **Functional Programming** | `map(lambda x: x*2,[1,2])` | `filter(lambda x:x>0,[-1,0,1])` | `reduce(add,[1,2,3])` | `partial(pow,2)(3)=8` |
|                            | `@lru_cache; fib(10)=55`     | `zip([1,2],[3,4])`            | `zip_longest([1],[2],fillvalue=0)` | `*args unpack: add(*[1,2])=3` |
|                            | `[x*x for x in range(3)]`    | `(x*x for x in range(3))`      | `[[x*y for y in range(3) if (x*y)%2==0] for x in range(3)]` | `count(10,2)→10,12…` |
|                            | `cycle('AB')→A B A…`         | `repeat('Hi',3)→'Hi'×3`        | `chain([1],[2])→[1,2]`            | `from_iterable([[1],[2]])` |
|                            | `takewhile(<3,[1,2,3])`      | `dropwhile(<2,[1,2,3])`        | `compress('ABC',[1,0,1])`         | `pairwise([1,2,3])` |
|                            | `combinations('ABC',2)`      | `permutations('ABC',2)`        | `product([1],[2])`                 | `accumulate([1,2,3])` |
|                            | `groupby('AAABBB')`          | `islice(range(10),2,5)→[2,3,4]` | `starmap(add,[(1,2)])→3`          |                        |
| **Collections**             | `namedtuple('Point','x y')` | `defaultdict(int)`              | `OrderedDict(a=1,b=2)`              | `Counter('aabbc')`      |
|                            | `deque([1,2,3])`            |                                |                                   |                        |
| **Datetime**                | `datetime.now()`            | `timedelta(days=5)`             |                                   |                        |
| **String & str Functions**  | `Template('Hi, $name')`      | `'a b'.split()`                 | `'-'.join(['a','b'])`              | `'abc'.find('b')`       |
|                            | `'abc'.replace('a','A')`     | `'ABC'.upper()/ 'abc'.lower()` |                                   |                        |
| **Regular Expressions (re)**| `re.search(r'\d+','a1b')`   | `re.findall(r'\w+','a1 b2')`   | `re.sub(r'\s','-','a b')`         | `match.groupdict()`     |
| **Heap Queue (heapq)**      | `heappush(heap,5); heappop(heap)` | `heapify([3,1,2])`         |                                   |                        |
| **Bisect**                  | `bisect_left([1,3,4],3)`    | `insort(list,2)`                |                                   |                        |
| **Enum**                    | `class Color(Enum): RED=1`   |                                |                                   |                        |
| **Pathlib**                 | `Path('.')`                  | `Path('.').exists()`            | `Path('file.txt').is_file()`        | `Path('.').is_dir()`     |
|                            | `Path('.').iterdir()`         | `Path('.').glob('*.py')`        | `Path('file.txt').read_text()`      | `Path('file.txt').write_text("Hi")` |
|                            | `Path('dir').mkdir()`         | `Path('dir').rmdir()`           | `Path('.').resolve()`               |                        |
| **Threading**               | `Thread(target=worker).start()` | `with Lock()/RLock():…`       | `with Semaphore(2):…`               | `Barrier(3).wait()`     |
|                            | `Condition().wait()/notify(), Event().set()` |                     |                                   |                        |
| **Concurrent Futures**      | `with ThreadPoolExecutor(3) as f: j = f.submit(g)` | `wait(j) / for x in as_completed(j)` |                             |                        |
| **URL & Basic HTTP**        | `urlparse(url)`               | `urlopen(url)`                  | `HTTPConnection('host')`             | `HTTPServer(('',8000),Handler)` |
| **Testing in Python**       | `unittest.main()`             | `def test(): assert f()==res`   | `pytest test_mod.py`                 |                        |
