#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>

/**
 * is_palindrome - function in C that checks
 * if a singly linked list is a palindrome
 * @head: the adress to the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int n, p, t, the_list;
	int *name;
	listint_t *current;
	listint_t  *new;

	current = *head;
	if (*head == NULL)
	{
		return (1);
	}
	n = 0;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}
	name = malloc(sizeof(int) * n);
	if (name == NULL)
	{
		return (0);
	}
	new = *head;
	for (p = 0; new != NULL && p < n; p++)
	{
		name[p] = new->n;
		new = new->next;
	}
	for (t = 0; t < n / 2; t++)
	{
		the_list = n - t - 1;
		if (name[t] != name[the_list])
		{
			free(name);
			return (0);
		}
	}
	free(name);
	return (1);
}
