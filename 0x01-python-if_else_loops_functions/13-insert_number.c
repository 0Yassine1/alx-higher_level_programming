#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of the head node of the list
 * @number: number to be inserted
 * Return: address of the new node, or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node, *current, *prev;
new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
return (NULL);

new_node->n = number;
new_node->next = NULL;

if (*head == NULL || (*head)->n >= number)
{
new_node->next = *head;
*head = new_node;
return (new_node);
}

prev = *head;
current = (*head)->next;

while (current != NULL && current->n < number)
{
prev = current;
current = current->next;
}
prev->next = new_node;
new_node->next = current;

return (new_node);
}