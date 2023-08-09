#include "lists.h"

/**
 * check_cycle - checks for linked list
 * @list: pointer
 * Return: 1 if cycle is found and 0 if cycle not found
 */
int check_cycle(listint_t *list)
{
	listint_t *current_node;
	listint_t *next_node;

	current_node = list;
	next_node = list->next;

	if (next_node != NULL || next_node != NULL)
	{
		if (current_node == next_node)
		{
			return (1);
		}
		current_node = current_node->next;
		next_node = (next_node->next)->next;

	}
	return (0);
}
