#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *no_cycle = list;
	listint_t *cycle = list;

	if (!list)
		return (0);

	while (no_cycle && cycle && cycle->next)
	{
		no_cycle = no_cycle->next;
		cycle = cycle->next->next;
		if (no_cycle == cycle)
			return (1);
	}

	return (0);
}
