#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAX_NODES 1000

struct Edge {
 int dest;
 int weight;
 struct Edge* next;
};

struct Graph {
 int num_nodes;
 struct Edge** adj_list;
};

struct MinHeapNode {
 int node;
 int key;
};

struct MinHeap {
 int size;
 int capacity;
 int* pos;
 struct MinHeapNode** array;
};

struct Graph* createGraph(int num_nodes) {
 struct Graph* graph = (struct Graph*) malloc(sizeof(struct Graph));
 graph->num_nodes = num_nodes;
 graph->adj_list = (struct Edge**) malloc(num_nodes * sizeof(struct Edge*));
 for (int i = 0; i < num_nodes; i++) {
 graph->adj_list[i] = NULL;
 }
 return graph;
}

void addEdge(struct Graph* graph, int src, int dest, int weight) {
 struct Edge* new_edge = (struct Edge*) malloc(sizeof(struct Edge));
 new_edge->dest = dest;
 new_edge->weight = weight;
 new_edge->next = graph->adj_list[src];
 graph->adj_list[src] = new_edge;
 
new_edge = (struct Edge*) malloc(sizeof(struct Edge));
 new_edge->dest = src;
 new_edge->weight = weight;
 new_edge->next = graph->adj_list[dest];
 graph->adj_list[dest] = new_edge;
}

struct MinHeapNode* createMinHeapNode(int node, int key) {
 struct MinHeapNode* min_heap_node = (struct MinHeapNode*) malloc(sizeof(struct MinHeapNode));
 min_heap_node->node = node;
 min_heap_node->key = key;
 return min_heap_node;
}

struct MinHeap* createMinHeap(int capacity) {
 struct MinHeap* min_heap = (struct MinHeap*) malloc(sizeof(struct MinHeap));
 min_heap->size = 0;
 min_heap->capacity = capacity;
 min_heap->pos = (int*) malloc(capacity * sizeof(int));
 min_heap->array = (struct MinHeapNode**) malloc(capacity * sizeof(struct MinHeapNode*));
 return min_heap;
}

void swapMinHeapNode(struct MinHeapNode** a, struct MinHeapNode** b) {
 struct MinHeapNode* temp = *a;
 *a = *b;
 *b = temp;
}

void minHeapify(struct MinHeap* min_heap, int idx) {
 int smallest, left, right;
 smallest = idx;
 left = 2 * idx + 1;
 right = 2 * idx + 2;

 if (left < min_heap->size && min_heap->array[left]->key < min_heap->array[smallest]->key) {
 smallest = left;
 }

 if (right < min_heap->size && min_heap->array[right]->key < min_heap->array[smallest]->key) {
 smallest = right;
 }

 if (smallest != idx) {
 struct MinHeapNode* smallest_node = min_heap->array[smallest];
 struct MinHeapNode* idx_node = min_heap->array[idx];

 min_heap->pos[smallest_node->node] = idx;
 min_heap->pos[idx_node->node] = smallest;

 swapMinHeapNode(&min_heap->array[smallest], &min_heap->array[idx]);
 minHeapify(min_heap, smallest);
 }
}

int* createMST(int num_nodes) {
    int* mst = (int*) malloc(num_nodes * sizeof(int));
    for (int i = 0; i < num_nodes; i++) {
        mst[i] = -1;
    }
    return mst;
}

int* primMST(struct Graph* graph) {
    int num_nodes = graph->num_nodes;
    int* mst = createMST(num_nodes);
    int* key = (int*) malloc(num_nodes * sizeof(int));
    int* in_heap = (int*) malloc(num_nodes * sizeof(int));
    struct MinHeap* min_heap = createMinHeap(num_nodes);

    for (int i = 1; i < num_nodes; i++) {
        key[i] = INT_MAX;
        in_heap[i] = 1;
        min_heap->array[i] = createMinHeapNode(i, key[i]);
        min_heap->pos[i] = i;
    }

    key[0] = 0;
    in_heap[0] = 1;
    min_heap->array[0] = createMinHeapNode(0, key[0]);
    min_heap->pos[0] = 0;
    min_heap->size = num_nodes;

    while (min_heap->size != 0) {
        struct MinHeapNode* min_heap_node = extractMin(min_heap);
        int u = min_heap_node->node;
        in_heap[u] = 0;
        struct Edge* edge = graph->adj_list[u];
        while (edge != NULL) {
            int v = edge->dest;
            if (in_heap[v] && edge->weight < key[v]) {
                key[v] = edge->weight;
                mst[v] = u;
                decreaseKey(min_heap, v, key[v]);
            }
            edge = edge->next;
        }
    }

    return mst;
}

struct MinHeapNode* extractMin(struct MinHeap* min_heap) {
    if (min_heap->size == 0) {
        return NULL;
    }

    struct MinHeapNode* root = min_heap->array[0];

    struct MinHeapNode* last_node = min_heap->array[min_heap->size - 1];
    min_heap->array[0] = last_node;

    min_heap->pos[root->node] = min_heap->size - 1;
    min_heap->pos[last_node->node] = 0;

    --min_heap->size;
    minHeapify(min_heap, 0);

    return root;
}

void decreaseKey(struct MinHeap* min_heap, int node, int key) {
    int i = min_heap->pos[node];
    min_heap->array[i]->key = key;

    while (i && min_heap->array[i]->key < min_heap->array[(i - 1) / 2]->key) {
        min_heap->pos[min_heap->array[i]->node] = (i - 1) / 2;
        min_heap->pos[min_heap->array[(i - 1) / 2]->node] = i;
        swapMinHeapNode(&min_heap->array[i], &min_heap->array[(i - 1) / 2]);
        i = (i - 1) / 2;
    }
}
