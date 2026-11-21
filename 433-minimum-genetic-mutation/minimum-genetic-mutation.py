class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        from collections import deque

        bank = set(bank)

        if endGene not in bank:
            return -1

        queue = deque([(startGene, 0)])
        visited = {startGene}

        genes = ['A', 'C', 'G', 'T']

        while queue:
            gene, steps = queue.popleft()

            if gene == endGene:
                return steps

            for i in range(len(gene)):
                for ch in genes:
                    new_gene = gene[:i] + ch + gene[i+1:]

                    if new_gene in bank and new_gene not in visited:
                        visited.add(new_gene)
                        queue.append((new_gene, steps + 1))

        return -1