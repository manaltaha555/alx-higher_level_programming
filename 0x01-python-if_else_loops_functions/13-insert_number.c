#include "lists.h"
/**
 *insert_node - function that inserts a node in sorted linkedlist
 *@head: pointer to the first element in the linked list
 *@number: value of the new node
 *Return: pointer to the new node
 *
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;
	listint_t *prev = node;
	listint_t *aft = node->next;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (node == NULL || node->n >= number)
        {
		new->next = node;
                *head = new;
                return(new);
        }
	while(prev && aft)
	{
		if (node->n < aft->n && node->n > prev->n)
		{
			prev->next = node;
			node->next = aft;
			return(node);
		}
		prev = prev->next;
		aft = aft->next;
	}
	return(node);

}
