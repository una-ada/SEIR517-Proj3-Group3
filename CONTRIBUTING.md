# Contributing to Tabby

## Task Organization

To keep tasks and progress organized, we're using both Trello and GitHub
Projects. Tasks that need to be done are added to the GH Project as Issues on
the repository:

1. Open the [issues tab](https://github.com/una-ada/Tabby/issues) on the repo.
2. Click on [new issue](https://github.com/una-ada/Tabby/issues/new).
3. The title should shortly describe the task to be done.
4. The description is only recommended and not completely necessary, but for
   some tasks a further explanation of what needs to be done can be included.
   This may also include links to reference materials for new features. For
   bugs, you should describe when and how the bug occurs and, if possible, where
   in the source code the bug comes form.
5. Assignees can be set by any contributor, and should be set to whoever is in
   charge of the relevant parts of the projects:
6. Labels can be set to describe what kind of task this is, most tasks will be
   marked as `feat` for feature requests and suggestions, followed by `fix` for
   bugs and other errors in the project.
7. The project for the issue should also be set for the current MVP project on
   the repo. If the "MVP" project does not show up immediately, click on the
   "repository" tab in the menu for assigning the issue to a project.
8. Milestones can also be set in the future, if we decide on future releases
   (e.g. "Version 1.1" for adding embedded maps).
9. Finally, click on the "Submit new issue" button.

Once an issue is added to the repo, it will also show up in the project board it
was assigned to. Since the current project is an automated Kanban-style board,
it should show up in the "To Do" column automatically. The issue can also be
attached to Trello cards using the GitHub power up.

If the power up is not currently added to the Trello board, it can be added
following these steps:

1. Open the Trello board.
2. If the board menu is not already open, click the "... Show menu" button in
   the top right corner.
3. In the third section of the menu, click the "Power-Ups" button.
4. On the left side of the Power-Ups dialog, type "GitHub" into the search
   field.
5. Select the "GitHub" power-up to add it.
6. Refer to
   [this page](https://help.trello.com/article/1065-using-the-github-power-up)
   for authenticating your GitHub account if it is not already connected to
   Trello.
7. Click the "Settings" button on the power-up card once it has been added.
8. Click "Edit Power-Up settings".
9. Click "Add repo".
10. Find the repo for this project and select it.

With the GitHub Power-Up added to the board, issues can be attached to cards
with the following steps:

1. Click the pencil button on the top-right of the card.
2. Click "Open Card".
3. In the "Power-Ups" section, click the "GitHub" button.
4. Click "Attach Issue..."
5. Select the issue you would like to attach; if it does not show up
   immediately, try searching by the issue number or title.
6. Once an issue is attached, if the settings on the Power-Up have not been
   changed, Trello will automatically add a comment to the issue with a link to
   the Trello card.

Closing issues should always be done via pull requests if it is not marked as
`wontfix` or `dupe`. To do this, an additional step is added to the pull request
process: adding attachment keywords to the description like
"Closes #&lt;issue number&gt;".

## Styleguides

### Git Commit Messages

- Use present tense ("add" not "added")
- Use imperative mood ("add" not "adds")
- Begin the title with a type and scope marker, i.e.
  `<type>(<scope>): <description>` using one of the following types:
  - `docs` for documentation (both embedded in code and separate files).
  - `feat` for adding a feature
  - `fix` for addressing issues, fixing bugs
  - `refactor` for rewriting existing features
  - `style` for fixing linting issues and other formatting errors
  - `infra` for adding boilerplate, importing libraries, or setting up CI and
    the like
- Keep the scope succinct, most updates should fall into one of these scopes:
  - `route` for URL routing
  - `model` for changes to the database models
  - `view` for view rendering and middleware directly connected to it
  - `ctrl` for controller functionality
  - `style` for updating CSS or adding images

### Python Styleguide

All Python code is linted with YAPF, see [.style.yapf](/.style.yapf) for the
exact settings. To enable auto-formatting in VS Code, install the
`ms-python.python` extension and change the `Python > Formatting: Provider`
setting to `yapf`.

1. Top level definitions should be divided by only a single line.

   ```python
   # Bad
   def foo():
   print('foo!')


   def bar():
     print('bar!')

   # Good
   def foo():
   print('foo!')

   def bar():
     print('bar!')
   ```

2. Braces should be coalesced to keep from making files unnecessarily vertical:

   ```python
   # Bad
   takes_a_dict(
     {
       'key_1': 'value_1',
       'key_2': 'value_2'
     }
   )

   # Good
   takes_a_dict({
     'key_1': 'value_1',
     'key_2': 'value_2'
   })
   ```

3. All lines should be limited to 80 columns wide. This can be visually
   indicated in VS Code by adding the following to your workspace or user
   `settings.json` file:

   ```json
   "editor.rulers": [ 80 ],
   ```

4. Closing braces should "dedent", i.e. be on the same column as the beginning
   of the line where the brace was opened:

   ```python
   # Bad
   some_dict = {
     'key_1': 'value_1',
     'key_2': 'value_2'
     }

   # Good
   some_dict = {
     'key_1': 'value_1',
     'key_2': 'value_2'
   }
   ```

5. Indentation should be done with 2 spaces:

   ```python
   # Bad
   if foo:
       bar()

   # Good
   if foo:
     bar()
   ```

6. All control blocks should be spread out into separate lines, not joined:

   ```python
   # Bad
   if foo: bar()

   # Good
   if foo:
     bar()
   ```

7. Comments following code lines should be tabbed to multiples of 8 for
   consistency and readability (i.e. starting on column 16, 24, 32, etc.)

   ```python
   # Bad
   colors = ('red', 'green', 'blue') # Define colors tuple
   print(len(colors))  # Use len() to get count

   # Good
   colors = ('red', 'green', 'blue')      # Define colors tuple
   print(len(colors))                     # Use len() to get count
   ```
