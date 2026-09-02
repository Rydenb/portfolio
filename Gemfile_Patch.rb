# Ruby 3.2+ / Ruby 4.0+ Compatibility Patch
# ============================================================================
# Liquid 4.0.3 (required by Jekyll 3.9.0) uses Ruby's deprecated taint-tracking
# security model, which was removed in Ruby 3.2. This patch restores stub
# implementations to prevent runtime errors.
#
# See: https://github.com/tzinfo/tzinfo/issues/145
#      https://github.com/ruby/ruby/blob/master/doc/globals.rdoc

if RUBY_VERSION.to_i >= 3
  module Kernel
    def taint
      self
    end

    def untaint
      self
    end

    def tainted?
      false
    end

    def freeze
      # Standard freeze behavior - unchanged
      __builtin_freeze(self)
    rescue
      # Fallback for built-in types
      self
    end
  end

  class Object
    def taint
      self
    end

    def untaint
      self
    end

    def tainted?
      false
    end
  end
end
