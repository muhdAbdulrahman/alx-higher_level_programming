#include "lists.h"

/**
 * check_cycle - function in C that checks if a singly linked list has a cycle in it
 * @list: the linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *point_1 = list;
	listint_t *check = list;

	if (list == NULL || list ->next == NULL)
		return (0);

	while (point_1 && check && check->next)
	{
		point_1 = point_1 -> next;
		check  = check->next->next;
		if (point_1 == check)
			return (1);
	}

	return (0);
}
