#  From Deep Learning Master to Two Pointers Disaster

## TIER 1: CRITICAL (90% de chance) 🔴
*Cai em TODA entrevista de DS. Foque aqui primeiro.*

### 1. Hash Maps and Sets (Chapter 2)
**Probabilidade:** 95% | **Pattern:** Lookup O(1) para evitar nested loops

**Gatilho mental DS:**
```
"preciso buscar/contar algo repetidamente? 
→ nested loop = O(n²) = morte
→ dict/set = O(1) lookup = salvação"
```

**Pattern correto:**
```python
# Frequency counter
freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1

# Existence check
seen = set(items)
if target in seen:  # O(1)
```

**Anti-pattern:**
```python
# ❌ ERRADO: nested loop
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] + arr[j] == target:  # O(n²)
```

**HackerRank problems:**
- Two Sum
- Check Magazine (ransom note)
- Hash Tables: Ice Cream Parlor
- Frequency Queries

---

### 2. Stacks (Chapter 7)
**Probabilidade:** 85% | **Pattern:** LIFO para processar sequências com ordem reversa

**Gatilho mental DS:**
```
"tem matching de pares/parenteses? → stack
tem navegação backward (undo/back)? → stack
preciso processar 'de dentro pra fora'? → stack"
```

**Pattern correto:**
```python
stack = []
for char in sequence:
    if is_opening(char):
        stack.append(char)  # push
    else:
        if not stack or not matches(stack[-1], char):
            return False
        stack.pop()  # pop
return len(stack) == 0
```

**Anti-pattern:**
```python
# ❌ ERRADO: usar lista + index manual
opened = []
closed = []
# muito verboso e propenso a erro
```

**HackerRank problems:**
- Balanced Brackets
- Simple Text Editor
- Maximum Element

---

### 3. Arrays + Two Pointers (Chapter 1)
**Probabilidade:** 80% | **Pattern:** Reduzir O(n²) para O(n) com ponteiros

**Gatilho mental DS:**
```
"array ordenado + busco par/tripla? → two pointers
preciso percorrer dos dois lados? → left/right pointers
janela deslizante fixa? → two pointers"
```

**Pattern correto:**
```python
left, right = 0, len(arr) - 1
while left < right:
    current = arr[left] + arr[right]
    if current == target:
        return [left, right]
    elif current < target:
        left += 1
    else:
        right -= 1
```

**Anti-pattern:**
```python
# ❌ ERRADO: O(n²) quando array já tá ordenado
for i in range(len(arr)):
    for j in range(i+1, len(arr)):  # desperdiça ordenação
```

**HackerRank problems:**
- Array Manipulation
- New Year Chaos
- Minimum Swaps 2

---

## TIER 2: HIGH PRIORITY (50-70% de chance) 🟡
*Provavelmente vai cair. Estude depois do Tier 1.*

### 4. Strings (implícito em vários chapters)
**Probabilidade:** 70% | **Pattern:** Manipulação + frequency counting

**Gatilho mental DS:**
```
"string é só array de chars
→ mesmos patterns de array funcionam
anagrama/permutação? → count characters com dict
substring? → sliding window"
```

**Pattern correto:**
```python
# Anagram check
from collections import Counter
Counter(s1) == Counter(s2)

# Character frequency
char_count = {}
for char in s:
    char_count[char] = char_count.get(char, 0) + 1
```

**HackerRank problems:**
- Sherlock and Anagrams
- Common Child
- Special String Again

---

### 5. Sliding Window (Chapter 5)
**Probabilidade:** 60% | **Pattern:** Janela dinâmica em arrays/strings

**Gatilho mental DS:**
```
"subarray/substring contínuo com condição? → sliding window
'longest/shortest satisfazendo X'? → window expansível
janela de tamanho fixo? → two pointers é melhor"
```

**Pattern correto:**
```python
left = 0
for right in range(len(arr)):
    # adiciona arr[right] na window
    while window_invalid():
        # remove arr[left] da window
        left += 1
    # atualiza resultado
```

**Anti-pattern:**
```python
# ❌ ERRADO: recalcular window inteira a cada step
for i in range(len(arr)):
    for j in range(i, len(arr)):
        window = arr[i:j+1]  # O(n³) com slicing
```

**HackerRank problems:**
- Maximum Subarray Sum
- Subarray Division

---

## TIER 3: MEDIUM PRIORITY (30-50% de chance) 🟢
*Pode cair mas não é essencial pra passar.*

### 6. Linked Lists (Chapter 3)
**Probabilidade:** 40% | **Pattern:** Manipulação de ponteiros

**Gatilho mental DS:**
```
"não é comum em DS interviews (mais SWE)
mas se cair: dummy node resolve 80% dos casos"
```

**Pattern correto:**
```python
dummy = ListNode(0)
dummy.next = head
current = dummy
while current.next:
    # manipula current.next
    current = current.next
return dummy.next
```

**HackerRank problems:**
- Insert a node at position
- Reverse a linked list
- Detect cycle

---

### 7. Trees (Chapter 11)
**Probabilidade:** 35% | **Pattern:** DFS/BFS recursivo

**Gatilho mental DS:**
```
"hierarquia? → tree
preciso nível por nível? → BFS (queue)
qualquer outra coisa? → DFS (recursão)"
```

**Pattern correto:**
```python
# DFS recursivo (mais comum)
def dfs(node):
    if not node:
        return
    # processa node
    dfs(node.left)
    dfs(node.right)
```

**HackerRank problems:**
- Tree: Height of Binary Tree
- Binary Search Tree: Insertion
- Tree: Level Order Traversal

---

## TIER 4: LOW PRIORITY (< 30%) ⚪
*Improvável para DS Senior. Só se sobrar tempo.*

### 8-11. Heaps, DP, Graphs, Backtracking
**Probabilidade:** 10-25% cada

**Gatilho mental DS:**
```
"muito avançado pra screening de DS
se cair → já erro e vou bem nas outras
não vale sacrificar o essencial por isso"
```

**Exceções:**
- **Heaps (Chapter 8):** Se pedirem "top K elements" → use heap
- **Graphs (Chapter 13):** Se for explicitamente sobre grafos → BFS/DFS básico
- **DP (Chapter 15):** Evite. Muito complexo pra tempo disponível

---

## ESTRATÉGIA DE EXECUÇÃO

### Semana 1 (hoje → screening):
1. **Dia 1-2:** Hash Maps (Tier 1.1) - resolva TODOS os problems do HackerRank listados
2. **Dia 3:** Stacks (Tier 1.2) - foco em Balanced Brackets
3. **Dia 4:** Arrays + Two Pointers (Tier 1.3)
4. **Dia 5:** Strings (Tier 2.1)
5. **Dia 6:** Sliding Window (Tier 2.2) OU revisão do Tier 1
6. **Dia 7:** Mock interview falando em voz alta

### Durante cada problema:
1. **Identifica o gatilho** (ex: "preciso buscar algo repetidamente")
2. **Mapeia pro pattern** (ex: "então dict/set")
3. **Implementa o snippet** (ex: freq counter)
4. **Evita o anti-pattern** (ex: não usa nested loop)

### Sinais de alerta (PARE e mude approach):
- ❌ Escrevendo 3+ loops nested → errado, tem pattern melhor
- ❌ Criando muitas variáveis temporárias → overengineering
- ❌ Código > 30 linhas para Easy problem → complicou demais
- ✅ Solução usa dict/set/stack E é < 20 linhas → provavelmente certo

---

## CHEAT SHEET FINAL

```python
# Se vejo isso no enunciado... penso nisso:

"find pair/duplicate" → dict ou set
"matching parentheses" → stack
"sorted array + target" → two pointers
"anagram/permutation" → Counter ou dict
"subarray/substring contínuo" → sliding window
"top K elements" → heap (mas improvável)
"shortest path" → BFS (mas improvável)

# Time complexity sanity check:
O(n) ou O(n log n) → provavelmente certo
O(n²) → só se for inevitável (matriz, etc)
O(2^n) ou O(n!) → errado, tem jeito melhor
```

priorize MUITO mais fazer os 10 problemas essenciais do Tier 1 perfeitamente do que fazer 50 problemas pela metade.