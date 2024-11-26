###### Done with ChatGPT xd
###### to help me remember of this methods if I ever need one I forgot...

# Special methods (magic methods) LOL, \_\_method\_\_ type thing

A list of **magic methods** (also known as **special methods** or **dunder methods**) that Python uses to define how objects of a class interact with built-in operators, functions, and methods. These are part of Python's **operator overloading** and **custom behavior** for various operations like addition, subtraction, multiplication, etc.

-    def \_\_sub\_\_(self, value: int, /) -> int: ...
-    def \_\_mul\_\_(self, value: int, /) -> int: ...
-    def \_\_floordiv\_\_(self, value: int, /) -> int: ...
-    def \_\_truediv\_\_(self, value: int, /) -> float: ...
-    def \_\_mod\_\_(self, value: int, /) -> int: ...
-    def \_\_divmod\_\_(self, value: int, /) -> tuple[int, int]: ...
-    def \_\_radd\_\_(self, value: int, /) -> int: ...
-    def \_\_rsub\_\_(self, value: int, /) -> int: ...
-    def \_\_rmul\_\_(self, value: int, /) -> int: ...
-    def \_\_rfloordiv\_\_(self, value: int, /) -> int: ...
-    def \_\_rtruediv\_\_(self, value: int, /) -> float: ...
-    def \_\_rmod\_\_(self, value: int, /) -> int: ...
-    def \_\_rdivmod\_\_(self, value: int, /) -> tuple[int, int]: ...

Are primarily related to **arithmetic operators** and **reflected operations**. These methods enable Python objects to work with built-in operations (e.g., `+`, `-`, `*`, `/`, etc.). Let's go through some more of these methods and categorize them:

### 1. **Arithmetic and Comparison Operators**
These methods enable Python objects to interact with arithmetic and comparison operators like `+`, `-`, `*`, `/`, etc.

- `__add__(self, other)` — **Addition (`+`)**
- `__sub__(self, other)` — **Subtraction (`-`)**
- `__mul__(self, other)` — **Multiplication (`*`)**
- `__floordiv__(self, other)` — **Floor division (`//`)**
- `__truediv__(self, other)` — **True division (`/`)**
- `__mod__(self, other)` — **Modulo (`%`)**
- `__divmod__(self, other)` — **Divmod (returns a tuple of quotient and remainder)**
  
**Reflected operators** (for reversed operations):
- `__radd__(self, other)` — **Reflected addition (`+`)**
- `__rsub__(self, other)` — **Reflected subtraction (`-`)**
- `__rmul__(self, other)` — **Reflected multiplication (`*`)**
- `__rfloordiv__(self, other)` — **Reflected floor division (`//`)**
- `__rtruediv__(self, other)` — **Reflected true division (`/`)**
- `__rmod__(self, other)` — **Reflected modulo (`%`)**
- `__rdivmod__(self, other)` — **Reflected divmod**

### 2. **Comparison Operators**

These methods allow objects to interact with comparison operators like `==`, `!=`, `>`, `<`, etc.

- `__eq__(self, other)` — **Equal to (`==`)**
- `__ne__(self, other)` — **Not equal to (`!=`)**
- `__lt__(self, other)` — **Less than (`<`)**
- `__le__(self, other)` — **Less than or equal to (`<=`)**
- `__gt__(self, other)` — **Greater than (`>`)**
- `__ge__(self, other)` — **Greater than or equal to (`>=`)**

### 3. **Unary Operations**

These methods allow for unary operators like `-`, `+`, `abs()`, etc.

- `__neg__(self)` — **Unary negation (`-`)**
- `__pos__(self)` — **Unary positive (`+`)**
- `__abs__(self)` — **Absolute value (`abs()`)**
- `__invert__(self)` — **Bitwise negation (`~`)**

### 4. **Container/Iterable Operations**

These methods are used for working with sequences and containers (e.g., lists, tuples, dictionaries, etc.):

- `__getitem__(self, key)` — **Item access (`[]`)**
- `__setitem__(self, key, value)` — **Item assignment (`[] =`)**
- `__delitem__(self, key)` — **Item deletion (`del []`)**
- `__iter__(self)` — **Iterator (`for item in obj`)**
- `__next__(self)` — **Iterator item access (`next()`)**
- `__contains__(self, item)` — **Membership test (`in`)**

### 5. **Object Representation and String Conversion**

These methods allow you to control how your objects are represented as strings or how they interact with `print()`, `str()`, etc.

- `__str__(self)` — **String representation (`str()`, `print()`)**
- `__repr__(self)` — **Formal string representation (`repr()`)**
- `__format__(self, format_spec)` — **Custom string formatting (`format()`)**

### 6. **Context Managers**

These methods allow you to define **context managers** (i.e., the behavior inside a `with` statement).

- `__enter__(self)` — **Start of the context manager (`with`)**
- `__exit__(self, exc_type, exc_value, traceback)` — **Exit of the context manager**

### 7. **Callable Objects**

These methods allow instances of a class to be used as if they were functions.

- `__call__(self, *args, **kwargs)` — **Function call syntax (`obj()`)**

### 8. **Descriptor Methods (for defining custom behavior when an attribute is accessed)**

These methods are used when defining custom behavior for attribute access, setting, and deletion.

- `__get__(self, instance, owner)` — **Attribute access**
- `__set__(self, instance, value)` — **Attribute assignment**
- `__delete__(self, instance)` — **Attribute deletion**

### 9. **Hashing and Equality**

These methods are used for **hashing** (e.g., for using objects as dictionary keys) and **equality**.

- `__hash__(self)` — **Object hash value (for using in sets and as dictionary keys)**
- `__eq__(self, other)` — **Equality comparison (`==`)**
- `__ne__(self, other)` — **Not equal comparison (`!=`)**

### 10. **Miscellaneous Operations**

- `__index__(self)` — **Index conversion for objects (used for slicing, `range()`, etc.)**
- `__del__()` — **Destructor method (called when an object is being deleted)**
- `__new__(cls, *args, **kwargs)` — **Object creation (called before `__init__`)**

### Full List of Common Magic Methods:

Here’s a non-exhaustive list of common magic methods:

- `__init__(self, ...)` — Constructor (initializes an object).
- `__del__(self)` — Destructor (called when the object is being deleted).
- `__repr__(self)` — Official string representation (used by `repr()`).
- `__str__(self)` — Informal string representation (used by `print()`).
- `__call__(self, ...)` — Allows an object to be called like a function.
- `__getitem__(self, key)` — Allows item access via `obj[key]`.
- `__setitem__(self, key, value)` — Allows item assignment via `obj[key] = value`.
- `__delitem__(self, key)` — Allows item deletion via `del obj[key]`.
- `__iter__(self)` — Makes an object iterable (used in `for` loops).
- `__next__(self)` — The next item for iteration.
- `__contains__(self, item)` — Checks if an item exists in an object (via `item in obj`).
- `__len__(self)` — Returns the length of the object (for `len(obj)`).
- `__abs__(self)` — Called by `abs()`.

### Conclusion

The methods listed are part of Python's **operator overloading** system, where you can define custom behavior for arithmetic and comparison operators, among others. Python has a whole set of these **magic methods** that allow you to control various aspects of how your objects behave in certain contexts, making it very flexible.