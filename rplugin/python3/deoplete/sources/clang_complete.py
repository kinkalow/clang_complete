#=============================================================================
# FILE: clang_complete.py
# AUTHOR: Joe Hermaszewski
#=============================================================================

from .base import Base

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'clang_complete'
        self.mark = '[CL]'
        self.filetypes = ['c', 'cpp', 'objc', 'objcpp']
        self.is_bytepos = True
        self.input_pattern = '[^. \t0-9]\.\w*'

    def get_complete_position(self, context):
        return self.vim.call('ClangComplete', 1, 0)

    def gather_candidates(self, context):
        dup = self.vim.eval('g:__my_clang_complete_duplicate')
        if dup:
          return self.vim.call('ClangComplete', 0, '')
        else:
          results = self.vim.call('ClangComplete', 0, '')
          items = []
          for result in results[:]:
            if result['abbr'] in items:
              results.remove(result)
            else:
              items.append(result['abbr'])
          return results
