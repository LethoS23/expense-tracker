Usage
=====

Once installed, you can start tracking expenses right away.

.. code-block:: python

   from tracker import ExpenseTracker
   tracker = ExpenseTracker("tracker.db")
   tracker.add_expense("Coffee", 3.5, "Food")

Use the command line to view summaries:

.. code-block:: bash

   python tracker.py --summary
